from django.db import models

# Create your models here.
class User(models.Model):
  discord_id = models.CharField(max_length=64)
  leetcode_id = models.CharField(max_length=128)

  class Meta:
    db_table = 'discord_users'


class Problem(models.Model):
  problem_id = models.CharField(max_length=256)
  problem_name = models.CharField(max_length=256)
  problem_description = models.TextField()
  difficulty_level = models.CharField(max_length=64)
  problem_url = models.URLField()

  times_chosen = models.IntegerField(default=0)
  last_chosen = models.DateTimeField(null=True)

  class Meta:
    db_table = 'leetcode_problems'


class SolvedProblems(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
  date_solved = models.DateTimeField(auto_now_add=True)

  solved_as_bounty_challenge = models.BooleanField(default=False)
  solved_as_daily_challenge = models.BooleanField(default=False)

  class Meta:
    db_table = 'solved_problems'
    unique_together = ('user', 'problem')

Problem.users_solved = models.ManyToManyField(User, through=SolvedProblems, related_name='problems_solved')


class DifficultyPoints(models.Model):
  difficulty_name = models

  class Meta:
    db_table = 'difficulty_points'
