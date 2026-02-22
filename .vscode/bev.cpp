#include <iostream>
using namespace std;

int main()
{
    /* -------------------- PART 1: Beverage Survey -------------------- */

    int coffee = 0, tea = 0, coke = 0, orangeJuice = 0;
    int choice;
    int person = 1;

    while (true)
    {
        cout << "Please input the favorite beverage of person #"
             << person
             << ": Choose 1, 2, 3, or 4 from the above menu or -1 to exit the program\n";

        cin >> choice;

        if (choice == -1)
            break;

        if (choice == 1)
            coffee++;
        else if (choice == 2)
            tea++;
        else if (choice == 3)
            coke++;
        else if (choice == 4)
            orangeJuice++;

        person++;
    }

    int totalPeople = person - 1;

    cout << "\nThe total number of people surveyed is " << totalPeople << ". The results are as follows:\n";
    cout << "Beverage\tNumber of Votes\n";
    cout << "********************************\n";
    cout << "Coffee\t\t" << coffee << endl;
    cout << "Tea\t\t" << tea << endl;
    cout << "Coke\t\t" << coke << endl;
    cout << "Orange Juice\t" << orangeJuice << endl;
}
