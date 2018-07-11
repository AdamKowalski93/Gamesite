from django.db import models

class GameModel(models.Model):
    Game_name=models.CharField(name='GameName',max_length=600)
    GameDiscryption=models.TextField(name='GameDiscryp')
    GameLink=models.CharField(name='GameLink',max_length=600)
    GameImage=models.CharField(name='GameImage',max_length=600)


