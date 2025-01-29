from django.db import models

# Create your models here.


class Game(models.Model):
    GENRE_CHOICES = (
        ("ACTION", "Action"),
        ("ADVENTURE", "Adventure"),
        ("RPG", "Role-Playing Game (RPG)"),
        ("JRPG", "Japanese Role-Playing Game"),
        ("STRATEGY", "Strategy"),
        ("SIMULATION", "Simulation"),
        ("SPORTS", "Sports"),
        ("PUZZLE", "Puzzle"),
        ("HORROR", "Horror"),
        ("PLATFORMER", "Platformer"),
        ("SHOOTER", "Shooter"),
        ("FIGHTING", "Fighting"),
        ("RACING", "Racing"),
        ("MMO", "Massively Multiplayer Online (MMO)"),
        ("SURVIVAL", "Survival"),
        ("SANDBOX", "Sandbox"),
        ("STEALTH", "Stealth"),
        ("MOBA", "Multiplayer Online Battle Arena (MOBA)"),
        ("RHYTHM", "Rhythm"),
        ("BATTLE_ROYALE", "Battle Royale"),
        ("OPEN_WORLD", "Open World"),
    )
    title = models.CharField(max_length=30)
    rating = models.IntegerField()
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, default="OTHER")
    release_date = models.DateField()
