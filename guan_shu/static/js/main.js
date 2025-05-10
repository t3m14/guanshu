// static/js/main.js
function toggleSideMenu() {
    const sideMenu = document.getElementById('sideMenu');
    sideMenu.classList.toggle('-translate-x-full');
}

// Обработчики для модальных окон
document.addEventListener('DOMContentLoaded', function() {
    // Buy modal logic
    const betSlider = document.getElementById('betSlider');
    const betInput = document.getElementById('betInput');
    const winAmountDisplay = document.getElementById('winAmount');
    
    function updateBetAmount() {
        const betAmount = parseInt(betInput.value);
        betSlider.value = betAmount;
        const winAmount = (betAmount * 1.471).toFixed(2);
        winAmountDisplay.textContent = winAmount;
    }
    
    if (betSlider && betInput && winAmountDisplay) {
        betSlider.addEventListener('input', function() {
            betInput.value = this.value;
            updateBetAmount();
        });
        
        betInput.addEventListener('input', function() {
            let value = parseInt(this.value);
            if (value < 0) value = 0;
            if (value > 100) value = 100;
            this.value = value;
            betSlider.value = value;
            updateBetAmount();
        });
    }
    
    // Close modals when clicking outside
    document.addEventListener('click', function(event) {
        const sideMenu = document.getElementById('sideMenu');
        const menuButton = document.querySelector('[onclick="toggleSideMenu()"]');
        
        if (!sideMenu.contains(event.target) && !menuButton.contains(event.target) && !sideMenu.classList.contains('-translate-x-full')) {
            sideMenu.classList.add('-translate-x-full');
        }
        
        // Buy modal
        const buyModal = document.getElementById('buyModal');
        if (buyModal && event.target === buyModal) {
            buyModal.classList.add('hidden');
        }
        
        // Add funds modal
        const addFundsModal = document.getElementById('addFundsModal');
        if (addFundsModal && event.target === addFundsModal) {
            addFundsModal.classList.add('hidden');
        }
    });
});

// Global functions for modals
function openBuyModal() {
    document.getElementById('buyModal').classList.remove('hidden');
}

function closeBuyModal() {
    document.getElementById('buyModal').classList.add('hidden');
}

function openAddFundsModal() {
    document.getElementById('addFundsModal').classList.remove('hidden');
    document.getElementById('sideMenu').classList.add('-translate-x-full');
}

function closeAddFundsModal() {
    document.getElementById('addFundsModal').classList.add('hidden');
}

function adjustBet(amount) {
    let currentBet = parseInt(document.getElementById('betInput').value);
    currentBet += amount;
    if (currentBet > 100) currentBet = 100;
    if (currentBet < 0) currentBet = 0;
    document.getElementById('betInput').value = currentBet;
    document.getElementById('betSlider').value = currentBet;
    updateBetAmount();
}