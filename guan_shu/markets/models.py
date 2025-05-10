from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MarketCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class Market(models.Model):
    YES = 'YES'
    NO = 'NO'
    MULTIPLE = 'MULTIPLE'
    
    OUTCOME_TYPES = [
        (YES, 'Yes/No'),
        (NO, 'No/Yes'),
        (MULTIPLE, 'Multiple outcomes'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(MarketCategory, on_delete=models.SET_NULL, null=True)
    outcome_type = models.CharField(max_length=10, choices=OUTCOME_TYPES, default=YES)
    created_at = models.DateTimeField(auto_now_add=True)
    resolution_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    volume = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    def __str__(self):
        return self.title

class MarketOutcome(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='outcomes')
    name = models.CharField(max_length=100)
    probability = models.DecimalField(max_digits=5, decimal_places=2)  # 0-100%
    
    def __str__(self):
        return f"{self.market.title} - {self.name}"

class UserBet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bets')
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    outcome = models.ForeignKey(MarketOutcome, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    potential_payout = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_win = models.BooleanField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} bet ${self.amount} on {self.outcome.name}"