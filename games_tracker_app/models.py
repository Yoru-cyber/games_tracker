from django.db import models

# Create your models here.


class Game(models.Model):
    STATUS_CHOICES = (
        ("FINISHED", "Finished"),
        ("PLAYING", "Playing"),
        ("PLANTOPLAY", "Plan to Play"),
        ("Other", "Other"),
    )
    GENRE_CHOICES = (
        ("ACTION", "Action"),
        ("ADVENTURE", "Adventure"),
        ("RPG", "Role-Playing Game"),
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
        ("OTHER", "Other"),
    )
    title = models.CharField(max_length=30)
    rating = models.IntegerField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Other")
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, default="Other")
    release_date = models.DateField()
