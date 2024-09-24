from django.shortcuts import render
import random
from django.contrib import messages

def index_view(request):
    return render(request, 'index.html') 

def game_view(request):
    return render(request, 'game.html')
    

def guessing_number_view(request):
    if request.method == "POST":
        user_choice = request.POST.get('choice')
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You win!"
        else:
            result = "You lose!"

        messages.info(request, f"You chose: {user_choice}. Computer chose: {computer_choice}. {result}")

    return render(request, 'game/guessing_number.html')
