#include <iostream>
#include <list>

using namespace std;

// Function prototype
int josephus(int numPeople, int eliminationCount);

int main() {
    // Get the number of people and elimination count from the user
    int numPeople, eliminationCount;
    cout<<"Welcome to the Josephus Problem game"<<endl;
    cout << "Enter the number of people: ";
    cin >> numPeople;
    cout << "Enter the elimination count: ";
    cin >> eliminationCount;

    // Calculate the winning participant
    int winner = josephus(numPeople, eliminationCount);

    // Display the winner
    std::cout << "The winning participant is: " << winner << std::endl;

    return 0;
}

int josephus(int numPeople, int eliminationCount) {
    // Create a linked list to represent the circle of people
    std::list<int> circle;
    for (int i = 1; i <= numPeople; ++i) {
        circle.push_back(i);
    }

    // Start the game
    auto current = circle.begin();
    while (circle.size() > 1) {
        // Find the next person to be eliminated
        for (int count = 1; count < eliminationCount; ++count) {
            ++current;
            if (current == circle.end()) {
                current = circle.begin();
            }
        }

        // Eliminate the current person
        current = circle.erase(current);

        // Wrap around if necessary
        if (current == circle.end()) {
            current = circle.begin();
        }
    }

    // Return the winning participant
    return *current;
}
