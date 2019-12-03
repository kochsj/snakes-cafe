# Snakes-Cafe

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
This application is a simulation of a point of sale for a restaurant. It is a script run in the command line. It asks the user to select a food that they would like to order prints what the food and quantity of food the user has ordered.

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
Make sure you have python3 installed:
```
$ python3 --version
```
If you do not:
```
$ brew install python
```
In your command line, navigate to this directory.

To run:
```
$ python3 snakes_cafe.py
```
Enter in your order!

## Architecture
When run, the program prints an intro message and the menu for the restaurant
The restaurant’s menu includes appetizers, entrees, desserts, and beverages
The program prompts the user for an order
When a user enters an item, the program prints an acknowledgment of their input
Further inputs update the total number in the order

## Change Log
Mon Dec 02 2019 15:26:27 - Added an intro message and menu that prints when script is run.
Mon Dec 02 2019 16:14:15 - Added functionality to 'order' and item and update the number of that item ordered.