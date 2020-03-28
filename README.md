# Distributions - A quick analysis of your data distribution in python!
Binomial and Normal Distribution
 

With Distributions, you can quickly analyze and visualize the distributions (Gaussian and Binomial) of your data with python with just few lines of code. Just specify the filename from which you would like to read data, and the rest is done for you.

# Overview
The Distributions Python package was written with fast use in mind. The package currently supports two distributions - Gaussain and Binomial. It provides the following key features

  - Read in dataset
  - Calculate mean, standard deviation
  - Plot histogram, probability density function
  - Add two distributions


## Usage

In the following paragraphs, I am going to describe how you can get and use Distributions for your own projects.

###  Getting it

To download distributions, fork this github repo. 

### Using it

Distributions was programmed with ease-of-use in mind. First, import Gaussian and Binomial from Distributions

```Python
from distributions import Gaussian
from distributions import Binomial
```

And you are ready to go! At this point, I want to clearly explain Gaussian and Binomial class objects. 

## Initialize a gaussian and binomial object
mu is the mean of distribution
sigma is the standard deviation of distribution
probablity of sucsess in binomial distribution
n is the number of trials/experiments

```Python
gaussian_one=Gaussian(mu,sigma) or
gaussian_one=Gaussian()

binomial_one=Binomial(mu,sigma,probability,n) or
binomial_one=Binomial()
```

## Read sample/population data
The class Gaussian and Binomial inherit methods of generic Distributions class. The distribution class has a method to initialize the
data with mean, standard deviation, and a list to save data. Another method is defined to take the file name as input to read the
.txt data. The second argument to the read_data_file is a boolean which takes True or False value depending upon if the data is 
sample or not respectively. 
This method also calls the methods that calculate the mean and standard deviation.

```Python
gaussian_one.read_data_file(file_name,True)
```

#### Plot histograms and/or probability density functions
For the given data there are methods that allow you to plot the histogram and probability density function for the given
range of data

```Python
gaussian_one.plot_histogram()
gaussian_one.plot_histogram_pdf()
```

### Magic methods
There are two magic methods included for both the distribution classes. You can add two objects and represent the class object with
the attributes of the class object.

```Python
gaussian_one + gaussian_two

```


License
----

MIT License

Copyright (c) 2020 Chaitanya Joshi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
