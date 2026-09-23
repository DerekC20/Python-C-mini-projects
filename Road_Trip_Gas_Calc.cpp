#include <iostream>

using namespace std;

int main() {

   // Variable declarations
    double milesDriven = 0.0;    // Total miles for the trip
    double gasPrice = 0.0;       // Cost of gas per gallon
    double vehicleMpg = 0.0;     // Fuel efficiency in miles per gallon
    int numPeople = 0;           // Total passengers splitting the cost

    double gallonsUsed = 0.0;    // Total gallons needed
    double totalCost = 0.0;      // Total cost of gas for the trip
    double costPerPerson = 0.0;  // Individual cost share

    // Program header and prompts
    cout << "ROAD TRIP GAS COST CALCULATOR" << endl;
    
    cout << "How many miles is your road trip: ";
    cin >> milesDriven;

    cout << "How much does gas cost per gallon: ";
    cin >> gasPrice;

    cout << "How efficient is your vehicle in miles/gal: ";
    cin >> vehicleMpg;

    cout << "How many people are going on the road trip: ";
    cin >> numPeople;

    // Calculations
    gallonsUsed = milesDriven / vehicleMpg;
    totalCost = gallonsUsed * gasPrice;
    costPerPerson = totalCost / numPeople;

    // Output results with required spacing
    cout << endl;
    cout << "RESULTS:" << endl;
    cout << "You will use this many gallons of gas:      " << gallonsUsed << endl;
    cout << "The cost of gas for the trip will be :       $" << totalCost << endl;
    cout << "The cost of gas per person will be :         $" << costPerPerson << endl;
    cout << endl;

    return 0;
}
