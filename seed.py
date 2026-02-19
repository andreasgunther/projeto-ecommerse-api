from app import create_app
from app.models import db, User, Product

# Cria a instância do app para acessar o banco
application = create_app()

def seed_database():
    with application.app_context():
        # Limpa o banco antes de começar
        print("Cleaning database")
        db.drop_all()
        db.create_all()

        # Cria usuarios
        user_comum = User(username="andreas", password="123")
        admin_user = User(username="admin", password="admin")
        db.session.add(user_comum)
        db.session.add(admin_user)
        print("Users created successfully")

        # Cria produtos exemplo
        p1 = Product(name="Arroz 5kg", price=25.50)
        p2 = Product(name="Feijão", price=9.90, description="Feijao top")
        p3 = Product(name="Teclado Gamer", price=250.00, description="switch mecanico")
        p4 = Product(name="Mouse", price=89.90, description="2.4Ghz")

        db.session.add_all([p1, p2, p3, p4])
        print("Products created successfully")

        # Salvando no arquivo
        db.session.commit()
        print("\nSeed completed, database ready to use")

if __name__ == "__main__":
    seed_database()