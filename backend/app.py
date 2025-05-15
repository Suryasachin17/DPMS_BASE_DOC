from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String, inspect
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:8080"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type"]
    }
})

# Database configuration
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@dpms-mysql:3306/dpms_db'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)

# Safe database initialization
def init_db():
    inspector = inspect(engine)
    if not inspector.has_table('persons'):
        Base.metadata.create_all(bind=engine)
        print("Created database tables")
    else:
        print("Tables already exist")

# Initialize database when app starts
init_db()

@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    
    db = SessionLocal()
    try:
        person = Person(name=name, age=age)
        db.add(person)
        db.commit()
        db.refresh(person)
        return jsonify({'status': 'success', 'id': person.id})
    except Exception as e:
        db.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)