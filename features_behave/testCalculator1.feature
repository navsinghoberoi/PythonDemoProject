@feature1
Feature: Test Calculator Basics
	@RegressionTest  @SanityTest
	Scenario: Add numbers via calculator
		Given : 2 integers
		When : sum method is called
		Then : It should return sum of numbers

	@RegressionTest
	Scenario: Multiply numbers via calculator
		Given : 2 integers
		When : multiply method is called
		Then : It should return product of numbers


