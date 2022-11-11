package cars

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
	return (float64(productionRate) / 100.0) * successRate
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
	return int(((float64(productionRate) / 100.0) * successRate) / 60.0)
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
	remainderOfCars := carsCount % 10
	remainderCost := remainderOfCars * 10000
	tensOfCars := carsCount / 10
	tensCost := tensOfCars * 95000
	totalCost := tensCost + remainderCost
	return uint(totalCost)
}
