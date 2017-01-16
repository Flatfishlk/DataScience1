import pickle
import numpy as np
import scipy.stats as scs

# Don't change this. This fixes the randomness in sampling
np.random.seed(seed=1234)


# This loads in the list of numbers you are going to deal with
def load_pickle(file_name):
    """INPUT:
    - file_name(STR) [The name of the file]

    OUTPUT:
    - population(NUMPY ARRAY) [A array of numbers for the exercise]
    """
    return pickle.load(open(file_name))


def draw_sample(population, n):
    """INPUT:
    - population(NUMPY ARRAY) [The array containing all the numbers]
    - n(INT) [The number of sample you wanna draw]

    OUTPUT:
    - sample(NUMPY ARRAY) [A array that contains a subset of the population]

    Hint: Use np.random.choice(). Google it. Google is your best friend
    """
    return np.random.choice(population, n)


def get_mean(lst):
    """INPUT:
    - lst(NUMPY ARRAY) [The array of numbers where we find the mean of]

    OUTPUT:
    - mean_value(FLOAT)

    Hint: Don't use np.mean().
    Then use np.mean(arr) to see if you got the same value
    """
    return np.average(lst)
# lst = np.arange(1,101,1).reshape(10,10)



def get_variance(lst, sample=True):
    """INPUT:
    - lst(NUMPY ARRAY) [Either the sample or the population]
    - sample(BOOL) [True if sample variance, False if population variance]

    OUTPUT:
    - lst_variance(FLOAT) [Sample or population variance depending]
    """
    sqdiff = 0.0
    Variance = 0.0
    if sample==False:
        for i in lst:
            sqdiff += (i - get_mean(lst))**2
        Variance = sum(sqdiff)/lst.size
        return Variance
    elif sample==True:
        for i in lst:
            sqdiff += (i - get_mean(lst))**2
        Variance = sum(sqdiff)/(lst.size-1)
        return Variance
# print get_variance(lst, sample = False)

def get_sem(sample):
    """INPUT:
    - sample(NUMPY ARRAY)

    OUTPUT:
    - sem(FLOAT) [Standard Error Mean]
    """
    return np.sqrt(get_variance(sample, sample=True))
# sample = lst
# print get_variance(sample, sample=True)
# print get_sem(sample)
# print np.std(sample)


def get_confidence_interval(sample, confidence=.95):
    """INPUT:
    - sample(NUMPY ARRAY)
    - confidence(FLOAT) [The confidence of the ci from 0 to 1, usually .95]

    OUTPUT:
    - (tuple) [mean, mean - half_rng, mean + half_rng]
    """
    m = get_mean(sample)
    v = get_sem(sample)
    interval = scs.t.ppf((1 - confidence)/2, sample.size - 1)
    half_rng = interval * np.sqrt(v) + m
    return m, m-half_rng, m+half_rng




def get_interquartile_range(population):
    """INPUT:
    - population(NUMPY ARRAY)

    OUTPUT:
    - iqr(FLOAT) [Interquartile range]
    """
    m = get_mean(population)
    v = get_sem(population)
    q75 = np.percentile(population, 75)
    q25 = np.percentile(population, 25)
    intquar = q75 - q25
    return q75, q25, intquar
# get_interquartile_range(sample)
# print scs.iqr(sample)


# convert = sample.flat
# for x in convert:
#     print x
# print ",".join(map(str, convert))
def get_outlier(population):
    """INPUT:
    - population(NUMPY ARRAY)

    OUTPUT:
    - outliers(NUMPY ARRAY) [List of outliers]
    """
    outliers = []
    q75 = np.percentile(population, 75)
    q25 = np.percentile(population, 25)
    convert = population.flat
    for i in convert:
        if i >= q75:
            outliers.append(i)
        if i <= q25:
            outliers.append(i)
    return outliers
# print get_outlier(sample)

if __name__ == '__main__':
    population = load_pickle('population.pkl')
    print 'First 10 element of the population: ', population[:10]
    sample_100 = draw_sample(population, 100)
    sample_1000 = draw_sample(population, 1000)
    population_mean = get_mean(population)
    sample_100_mean = get_mean(sample_100)
    sample_1000_mean = get_mean(sample_1000)
    print 'Population mean: ', population_mean
    print 'Sample 100 mean: ', sample_100_mean
    print 'Sample 1000 mean: ', sample_1000_mean
