@feature2
Feature: Test Calculator Advanced
	@RegressionTest  @SanityTest
	Scenario: Subtract numbers via calculator
		Given : 2 integers
		When : subtract method is called
		Then : It should return difference of numbers

	@RegressionTest
	Scenario: Divide numbers via calculator
		Given : 2 integers
		When : divide method is called
		Then : It should return result of division