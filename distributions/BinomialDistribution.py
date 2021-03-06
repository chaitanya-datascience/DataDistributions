# Import necessary libraries
import math
import matplotlib.pyplot as plt
from .GeneralDistribution import Distribution

# Make a Binomial class that inherits from the Distribution class. Use the specifications below.
class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring

    """

    #       A binomial distribution is defined by two variables:
    #           the probability of getting a positive outcome
    #           the number of trials

    #       If you know these two values, you can calculate the mean and the standard deviation
    #
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))

    #

    # Define the init function

        # Store the probability of the distribution in an instance variable p
        # Store the size of the distribution in an instance variable n

        # Now that you know p and n, you can calculate the mean and standard deviation
        #       You can use the calculate_mean() and calculate_stdev() methods defined below along with the __init__ function 
        # from the Distribution class

    def __init__(self,prob=0.5,n=10):
        self.p=prob
        self.n=n
        Distribution.__init__(self,0,1)

    # Write a method calculate_mean() according to the specifications below
    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
        self.mean= self.p*self.n
        return self.mean


    # Write a calculate_stdev() method accordin to the specifications below.
    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """
        self.stdev=math.sqrt(self.n*self.p*(1-self.p))
        return self.stdev

    # The read_data_file() from the Generaldistribution class can read in a data
    # file. Because the Binomaildistribution class inherits from the Generaldistribution class,
    # you don't need to re-write this method. However,  the method
    # doesn't update the mean or standard deviation of
    # a distribution. Hence a method that calculates n, p, mean and
    # standard deviation from a data set and then updates the n, p, mean and stdev attributes is added.
    #
    #       The code:
    #           updates the n attribute of the binomial distribution
    #           updates the p value of the binomial distribution by calculating the
    #               number of positive trials divided by the total trials
    #           updates the mean attribute
    #           updates the standard deviation attribute
    #
    def replace_stats_with_data(self):

        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
        self.n=len(self.data)
        self.p=len([i for i in self.data if i==1])/self.n
        self.mean=self.calculate_mean()
        self.stdev=self.calculate_stdev()
        return self.p,self.n

    # A method plot_bar() that outputs a bar chart of the data set according to the following specifications.
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        plt.hist(self.data)
        plt.xlabel('Data')
        plt.ylabel('Count')
        plt.title('Histogram of data')
        plt.show()

    #Calculate the probability density function of the binomial distribution
    def pdf(self,k):
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
        return math.factorial(self.n)/(math.factorial(k)*math.factorial(self.n-k))*self.p**k*(1-self.p)**(self.n-k)

    # A method to plot the probability density function of the binomial distribution
    def plot_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        # Use a bar chart to plot the probability density function from
        # k = 0 to k = n

        #   This method also returns the x and y values used to make the chart
        #   The x and y values are stored in separate lists
        x=[]
        y=[]
        k=self.n
        for success in range(k):
            x.append(k)
            y.apped(self.pdf(self,k))

        x_pos = [i for i, _ in enumerate(x)]
        # plot
        plt.bar(x,y,color='blue')
        plt.title('Bionoimal Probability Density Function')
        plt.xlabel('Number of sucesses')
        plt.ylabel('Density')
        plt.xticks(x_pos, x)
        plt.show()

        return x,y






    # A method to output the sum of two binomial distributions. Assumes that both distributions have the same p value.
    def __add__(self,other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        results=Binomial()
        results.p=self.p
        results.n=self.n+other.n
        return results
        # Addition for two binomial distributions. Assumed that the
        # p values of the two distributions are the same. The formula for
        # summing two binomial distributions with different p values is more complicated,
        # so only implemented the case for two distributions with equal p.

        # the try, except statement above will raise an exception if the p values are not equal

    # Using the __repr__ magic method to output the characteristics of the binomial distribution object.
    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """

        # Defined the representation method so that the output looks like
        #       mean 5, standard deviation 4.5, p .8, n 20
        #       with the values replaced by whatever the actual distributions values are
        #       The method should return a string in the expected format

        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean,self.stdev,self.p,self.n)
