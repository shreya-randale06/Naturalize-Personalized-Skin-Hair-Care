from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from models.models import db, User, SkinAssessment, HairAssessment
from ai_engine import AIEngine
from config import Config
import re
import json

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login to access this page.'

# Initialize AI Engine
ai_engine = AIEngine()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not name or not email or not password:
            flash('All fields are required.', 'danger')
            return redirect(url_for('signup'))
        
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('signup'))
        
        if len(password) < 6:
            flash('Password must be at least 6 characters.', 'danger')
            return redirect(url_for('signup'))
        
        # Check if user exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please login.', 'danger')
            return redirect(url_for('login'))
        
        # Create new user
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(name=name, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash(f'Welcome back, {user.name}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/skin-assessment', methods=['GET', 'POST'])
@login_required
def skin_assessment():
    if request.method == 'POST':
        try:
            # Only get these specific fields
            age = int(request.form.get('age'))
            if age < 0 or age > 120:
                flash('Please enter a valid age (0-120).', 'danger')
                return redirect(url_for('skin_assessment'))
            
            skin_type = request.form.get('skin_type')
            skin_tone = request.form.get('skin_tone')
            concerns = request.form.get('concerns')
            
            # Validate all fields are present
            if not all([age, skin_type, skin_tone, concerns]):
                flash('All fields are required.', 'danger')
                return redirect(url_for('skin_assessment'))
            
            # Print for debugging
            print(f"Skin Assessment - Age: {age}, Type: {skin_type}, Tone: {skin_tone}, Concerns: {concerns}")
            
            # Save assessment
            assessment = SkinAssessment(
                user_id=current_user.id,
                age=age,
                skin_type=skin_type,
                skin_tone=skin_tone,
                concerns=concerns
            )
            db.session.add(assessment)
            db.session.commit()
            
            # Get AI recommendations
            recommendations = ai_engine.generate_skin_recommendations(
                age, skin_type, skin_tone, concerns
            )
            
            # Save recommendations to database
            assessment.recommendations = json.dumps(recommendations)
            db.session.commit()
            
            return render_template('skin_result.html', 
                                 recommendations=recommendations,
                                 assessment=assessment)
            
        except ValueError as e:
            flash('Please enter a valid age number.', 'danger')
            return redirect(url_for('skin_assessment'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('skin_assessment'))
    
    return render_template('skin_assessment.html')

@app.route('/hair-assessment', methods=['GET', 'POST'])
@login_required
def hair_assessment():
    if request.method == 'POST':
        try:
            # Only get these specific fields
            hair_type = request.form.get('hair_type')
            hair_texture = request.form.get('hair_texture', '')
            hair_length = request.form.get('hair_length', '')
            concerns = request.form.get('concerns')
            
            # Combine concerns with texture and length if provided
            full_concerns = concerns
            if hair_texture:
                full_concerns += f", {hair_texture} texture"
            if hair_length:
                full_concerns += f", {hair_length} length"
            
            # Validate
            if not all([hair_type, concerns]):
                flash('Hair type and concerns are required.', 'danger')
                return redirect(url_for('hair_assessment'))
            
            # Print for debugging
            print(f"Hair Assessment - Type: {hair_type}, Concerns: {full_concerns}")
            
            # Save assessment
            assessment = HairAssessment(
                user_id=current_user.id,
                hair_type=hair_type,
                concerns=full_concerns
            )
            db.session.add(assessment)
            db.session.commit()
            
            # Get AI recommendations
            recommendations = ai_engine.generate_hair_recommendations(
                hair_type, full_concerns
            )
            
            # Save recommendations to database
            assessment.recommendations = json.dumps(recommendations)
            db.session.commit()
            
            return render_template('hair_result.html', 
                                 recommendations=recommendations,
                                 assessment=assessment)
            
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('hair_assessment'))
    
    return render_template('hair_assessment.html')

@app.route('/regenerate-skin/<int:assessment_id>')
@login_required
def regenerate_skin(assessment_id):
    assessment = SkinAssessment.query.get_or_404(assessment_id)
    
    if assessment.user_id != current_user.id:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('dashboard'))
    
    # Regenerate recommendations
    recommendations = ai_engine.generate_skin_recommendations(
        assessment.age,
        assessment.skin_type,
        assessment.skin_tone,
        assessment.concerns
    )
    
    # Update database
    assessment.recommendations = json.dumps(recommendations)
    db.session.commit()
    
    flash('Recommendations regenerated successfully!', 'success')
    return render_template('skin_result.html', 
                         recommendations=recommendations,
                         assessment=assessment)

@app.route('/regenerate-hair/<int:assessment_id>')
@login_required
def regenerate_hair(assessment_id):
    assessment = HairAssessment.query.get_or_404(assessment_id)
    
    if assessment.user_id != current_user.id:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('dashboard'))
    
    # Regenerate recommendations
    recommendations = ai_engine.generate_hair_recommendations(
        assessment.hair_type,
        assessment.concerns
    )
    
    # Update database
    assessment.recommendations = json.dumps(recommendations)
    db.session.commit()
    
    flash('Recommendations regenerated successfully!', 'success')
    return render_template('hair_result.html', 
                         recommendations=recommendations,
                         assessment=assessment)
@app.route('/general-care')
@login_required
def general_care():
    """Show general wellness and natural care tips"""
    return render_template('general_care.html')

if __name__ == '__main__':
    app.run(debug=True)