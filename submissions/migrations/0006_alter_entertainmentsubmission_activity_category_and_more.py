# Generated by Django 5.0.1 on 2024-02-27 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submissions", "0005_alter_entertainmentsubmission_activity_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entertainmentsubmission",
            name="activity_category",
            field=models.CharField(
                choices=[
                    ("Other", "Other"),
                    ("Amusement parks", "Amusement parks"),
                    (
                        "Arcades with kid-friendly games",
                        "Arcades with kid-friendly games",
                    ),
                    (
                        "Beaches or lakes for water activities",
                        "Beaches or lakes for water activities",
                    ),
                    ("Botanical gardens", "Botanical gardens"),
                    ("Bowling alleys", "Bowling alleys"),
                    ("Cafes with play areas", "Cafes with play areas"),
                    ("Children's shows or events", "Children's shows or events"),
                    ("Community sports events", "Community sports events"),
                    (
                        "Educational workshops or classes",
                        "Educational workshops or classes",
                    ),
                    (
                        "Gaming centers or esports arenas",
                        "Gaming centers or esports arenas",
                    ),
                    ("Indoor play areas", "Indoor play areas"),
                    ("Interactive science centers", "Interactive science centers"),
                    ("Live theaters or performances", "Live theaters or performances"),
                    ("Local events or festivals", "Local events or festivals"),
                    ("Local markets or fairs", "Local markets or fairs"),
                    ("Mini-golf courses", "Mini-golf courses"),
                    ("Movie theaters", "Movie theaters"),
                    ("Museums", "Museums"),
                    ("Nature trails or hiking spots", "Nature trails or hiking spots"),
                    ("Parks and playgrounds", "Parks and playgrounds"),
                    (
                        "Parades or community gatherings",
                        "Parades or community gatherings",
                    ),
                    ("Picnic areas", "Picnic areas"),
                    ("Planetariums", "Planetariums"),
                    ("Professional Sporting Event", "Professional Sporting Event"),
                    (
                        "Shopping centers with kid-friendly stores",
                        "Shopping centers with kid-friendly stores",
                    ),
                    (
                        "Sports complexes (for other sports)",
                        "Sports complexes (for other sports)",
                    ),
                    ("Swimming pools or water parks", "Swimming pools or water parks"),
                    ("Toy stores", "Toy stores"),
                    ("Trampoline parks", "Trampoline parks"),
                    ("Zoos and aquariums", "Zoos and aquariums"),
                ],
                default="Museums",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="restaurantsubmission",
            name="food_type",
            field=models.CharField(
                choices=[
                    ("Other", "Other"),
                    ("American", "American"),
                    ("Buffet", "Buffet"),
                    ("Chinese", "Chinese"),
                    ("Indian", "Indian"),
                    ("Italian", "Italian"),
                    ("Japanese", "Japanese"),
                    ("Korean", "Korean"),
                    ("Mediterranean", "Mediterranean"),
                    ("Mexican", "Mexican"),
                    ("Thai", "Thai"),
                ],
                default="American",
                max_length=20,
            ),
        ),
    ]
