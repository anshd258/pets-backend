from database.database import get_database
from models.models import Pet


pets_data = [
    {
        "name": "Max",
        "age": 3,
        "price": 250.0,
        "breed": "Golden Retriever",
        "description": "Max is a friendly and energetic Golden Retriever who loves to play fetch and go for long walks. He's great with kids and other pets.",
        "image_url": "https://images.unsplash.com/photo-1552053831-71594a27632d",
        "species": "Dog",
        "gender": "Male",
        "size": "Large",
        "status": "adoptable"
    },
    {
        "name": "Luna",
        "age": 2,
        "price": 200.0,
        "breed": "Persian",
        "description": "Luna is a beautiful Persian cat with a calm and affectionate personality. She loves to cuddle and be groomed.",
        "image_url": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131",
        "species": "Cat",
        "gender": "Female",
        "size": "Medium",
        "status": "adoptable"
    },
    {
        "name": "Charlie",
        "age": 4,
        "price": 300.0,
        "breed": "Beagle",
        "description": "Charlie is a playful Beagle with a nose for adventure. He's well-trained and loves treats!",
        "image_url": "https://images.unsplash.com/photo-1505628346881-b72b27e84530",
        "species": "Dog",
        "gender": "Male",
        "size": "Medium",
        "status": "adoptable"
    },
    {
        "name": "Bella",
        "age": 1,
        "price": 180.0,
        "breed": "Siamese",
        "description": "Bella is a young Siamese cat with striking blue eyes. She's curious and loves to explore.",
        "image_url": "https://images.unsplash.com/photo-1573865526739-10659fec78a5",
        "species": "Cat",
        "gender": "Female",
        "size": "Small",
        "status": "adoptable"
    },
    {
        "name": "Rocky",
        "age": 5,
        "price": 350.0,
        "breed": "German Shepherd",
        "description": "Rocky is a loyal and protective German Shepherd. He's well-trained and perfect for an active family.",
        "image_url": "https://images.unsplash.com/photo-1568572933382-74d440642117",
        "species": "Dog",
        "gender": "Male",
        "size": "Large",
        "status": "adoptable"
    },
    {
        "name": "Daisy",
        "age": 2,
        "price": 220.0,
        "breed": "Labrador",
        "description": "Daisy is a sweet Labrador who loves water and swimming. She's gentle and patient with children.",
        "image_url": "https://images.unsplash.com/photo-1554224311-beee415c201f",
        "species": "Dog",
        "gender": "Female",
        "size": "Large",
        "status": "adoptable"
    },
    {
        "name": "Milo",
        "age": 3,
        "price": 190.0,
        "breed": "Maine Coon",
        "description": "Milo is a majestic Maine Coon with a fluffy coat. He's independent but loves attention on his terms.",
        "image_url": "https://images.unsplash.com/photo-1574158622682-e40e69881006",
        "species": "Cat",
        "gender": "Male",
        "size": "Large",
        "status": "adoptable"
    },
    {
        "name": "Cooper",
        "age": 2,
        "price": 280.0,
        "breed": "Corgi",
        "description": "Cooper is an adorable Corgi with short legs and a big personality. He's playful and loves to herd.",
        "image_url": "https://images.unsplash.com/photo-1546975490-e8b92a360b24",
        "species": "Dog",
        "gender": "Male",
        "size": "Small",
        "status": "adoptable"
    },
    {
        "name": "Lucy",
        "age": 4,
        "price": 160.0,
        "breed": "Tabby",
        "description": "Lucy is a friendly Tabby cat who gets along with everyone. She's low-maintenance and loves to nap.",
        "image_url": "https://images.unsplash.com/photo-1519052537078-e6302a4968d4",
        "species": "Cat",
        "gender": "Female",
        "size": "Medium",
        "status": "adoptable"
    },
    {
        "name": "Duke",
        "age": 6,
        "price": 400.0,
        "breed": "Husky",
        "description": "Duke is a stunning Husky with ice-blue eyes. He needs an active owner who loves outdoor adventures.",
        "image_url": "https://images.unsplash.com/photo-1547407139-3c921a66005c",
        "species": "Dog",
        "gender": "Male",
        "size": "Large",
        "status": "adoptable"
    },
    {
        "name": "Oliver",
        "age": 2,
        "price": 175.0,
        "breed": "British Shorthair",
        "description": "Oliver is a chunky British Shorthair with a plush coat. He's calm and loves lounging in sunny spots.",
        "image_url": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba",
        "species": "Cat",
        "gender": "Male",
        "size": "Medium",
        "status": "adoptable"
    },
    {
        "name": "Sophie",
        "age": 3,
        "price": 320.0,
        "breed": "Poodle",
        "description": "Sophie is an elegant Standard Poodle with a hypoallergenic coat. She's intelligent and easy to train.",
        "image_url": "https://images.unsplash.com/photo-1558788353-f76d92427f16",
        "species": "Dog",
        "gender": "Female",
        "size": "Large",
        "status": "adoptable"
    },
    {
        "name": "Simba",
        "age": 1,
        "price": 210.0,
        "breed": "Bengal",
        "description": "Simba is an exotic Bengal cat with leopard-like spots. He's active and loves climbing.",
        "image_url": "https://images.unsplash.com/photo-1545249390-6bdfa286032f",
        "species": "Cat",
        "gender": "Male",
        "size": "Medium",
        "status": "adoptable"
    },
    {
        "name": "Bailey",
        "age": 4,
        "price": 270.0,
        "breed": "Cocker Spaniel",
        "description": "Bailey is a gentle Cocker Spaniel with silky ears. She's affectionate and great with families.",
        "image_url": "https://images.unsplash.com/photo-1598133894008-61f7fdb8cc3a",
        "species": "Dog",
        "gender": "Female",
        "size": "Medium",
        "status": "adoptable"
    },
    {
        "name": "Shadow",
        "age": 5,
        "price": 150.0,
        "breed": "Black Cat Mix",
        "description": "Shadow is a mysterious black cat with golden eyes. Despite superstitions, he's incredibly lucky to have around.",
        "image_url": "https://images.unsplash.com/photo-1529778873920-4da4926a72c2",
        "species": "Cat",
        "gender": "Male",
        "size": "Medium",
        "status": "adoptable"
    },
    {
        "name": "Zeus",
        "age": 3,
        "price": 450.0,
        "breed": "Great Dane",
        "description": "Zeus is a gentle giant Great Dane. Despite his size, he thinks he's a lap dog and loves cuddles.",
        "image_url": "https://images.unsplash.com/photo-1585559700398-1385b3a8aeb6",
        "species": "Dog",
        "gender": "Male",
        "size": "Extra Large",
        "status": "adoptable"
    },
    {
        "name": "Cleo",
        "age": 2,
        "price": 195.0,
        "breed": "Ragdoll",
        "description": "Cleo is a beautiful Ragdoll cat with blue eyes. She goes limp when picked up and loves being held.",
        "image_url": "https://images.unsplash.com/photo-1513360371669-4adf3dd7dff8",
        "species": "Cat",
        "gender": "Female",
        "size": "Large",
        "status": "adoptable"
    },
    {
        "name": "Bruno",
        "age": 4,
        "price": 290.0,
        "breed": "Boxer",
        "description": "Bruno is an energetic Boxer who loves to play. He's loyal and makes an excellent family protector.",
        "image_url": "https://images.unsplash.com/photo-1543466835-00a7907e9de1",
        "species": "Dog",
        "gender": "Male",
        "size": "Large",
        "status": "adoptable"
    },
    {
        "name": "Mittens",
        "age": 1,
        "price": 140.0,
        "breed": "Tuxedo Cat",
        "description": "Mittens is a dapper tuxedo cat with white paws. She's playful and loves chasing laser pointers.",
        "image_url": "https://images.unsplash.com/photo-1548247416-ec66f4900b2e",
        "species": "Cat",
        "gender": "Female",
        "size": "Small",
        "status": "adoptable"
    },
    {
        "name": "Thor",
        "age": 2,
        "price": 380.0,
        "breed": "Australian Shepherd",
        "description": "Thor is a brilliant Australian Shepherd with striking blue eyes. He needs mental stimulation and loves agility training.",
        "image_url": "https://images.unsplash.com/photo-1542206395-9feb3edaa68d",
        "species": "Dog",
        "gender": "Male",
        "size": "Medium",
        "status": "adoptable"
    },
    {
        "name": "Nala",
        "age": 3,
        "price": 165.0,
        "breed": "Calico",
        "description": "Nala is a beautiful calico cat with a sassy personality. She's independent but affectionate with her chosen person.",
        "image_url": "https://images.unsplash.com/photo-1592194996308-7b43878e84a6",
        "species": "Cat",
        "gender": "Female",
        "size": "Medium",
        "status": "adoptable"
    },
    {
        "name": "Rex",
        "age": 5,
        "price": 260.0,
        "breed": "Rottweiler",
        "description": "Rex is a powerful Rottweiler with a heart of gold. He's protective but gentle with proper training.",
        "image_url": "https://images.unsplash.com/photo-1567225557594-88d73e55f2cb",
        "species": "Dog",
        "gender": "Male",
        "size": "Large",
        "status": "adoptable"
    },
    {
        "name": "Whiskers",
        "age": 7,
        "price": 120.0,
        "breed": "Senior Tabby",
        "description": "Whiskers is a wise senior cat looking for a quiet retirement home. He's low-energy and loves lap time.",
        "image_url": "https://images.unsplash.com/photo-1488740304459-45c4277e7daf",
        "species": "Cat",
        "gender": "Male",
        "size": "Medium",
        "status": "adoptable"
    },
    {
        "name": "Stella",
        "age": 2,
        "price": 310.0,
        "breed": "Border Collie",
        "description": "Stella is an incredibly smart Border Collie. She needs an active owner who can keep up with her intelligence.",
        "image_url": "https://images.unsplash.com/photo-1503256207526-0d5d80fa2f47",
        "species": "Dog",
        "gender": "Female",
        "size": "Medium",
        "status": "adoptable"
    },
    {
        "name": "Ginger",
        "age": 4,
        "price": 155.0,
        "breed": "Orange Tabby",
        "description": "Ginger is a friendly orange tabby with a big appetite. She's social and loves meeting new people.",
        "image_url": "https://images.unsplash.com/photo-1478098711619-5ab0b478d6e6",
        "species": "Cat",
        "gender": "Female",
        "size": "Medium",
        "status": "adoptable"
    }
]


async def seed_database():
    db = get_database()
    
    existing_pets = await db.pets.count_documents({})
    if existing_pets > 0:
        print(f"Database already has {existing_pets} pets. Skipping seed.")
        return
    
    pets_to_insert = []
    
    for pet_data in pets_data:
        pet = Pet(
            name=pet_data["name"],
            age=pet_data["age"],
            price=pet_data["price"],
            breed=pet_data["breed"],
            description=pet_data["description"],
            image_url=pet_data["image_url"],
            species=pet_data["species"],
            gender=pet_data["gender"],
            size=pet_data["size"],
            status=pet_data["status"],
            is_adopted=False
        )
        
        pet_dict = pet.dict(by_alias=True)

        pets_to_insert.append(pet_dict)
    
    await db.pets.insert_many(pets_to_insert)
    print(f"Successfully seeded {len(pets_to_insert)} pets into the database")

