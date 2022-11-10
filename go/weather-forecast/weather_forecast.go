// Package weather forcasts current weather condtions for Goblinocus.
package weather

// CurrentCondition represents the current weather condition.
var CurrentCondition string

// CurrentLocation represents a certain city in Goblinocus.
var CurrentLocation string

// Forecast returns a string value that explains the current Weather
// in a certain location in Goblinocus.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
