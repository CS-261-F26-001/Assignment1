# Homework 1: Earthquake Research

## Context

In this assignment, we will analyze past earthquakes using a real-world 
dataset. You will get some practice with Python fundamentals used throughout this course, and start learning to explain code efficiency using Big-O notation.

> [!TIP]
> If you get stuck on anything like reading a CSV file, binary search, or Big-O notation, check back through previous labs first. You can also come to office hours or ask the mailing list for help. The same resource restrictions from lab apply: only course materials, the [Python documentation](https://docs.python.org/3/), and code from previous labs and assignments. AI tools are not allowed.


## Part 1: Earthquake investigation

The homework repository comes with a template Python file `earthquake.py`, 
and a dataset `earthquakes.csv` which contains the earthquake data you will analyze. Review this file to ensure you understand the underlying dataset. The file contains a chronologically-sorted list of earthquakes, one per line. Each earthquake has several fields, including:
    
- id
- impact.magnitude
- impact.significance
- location.depth
- location.distance
- location.latitude
- location.longitude
- location.name
- time.epoch
- time.full

**Note:** there are many possible solutions and some are more efficient than others. You **do not** need to find the most efficient approach for each problem, just a correct solution that doesn't time out. You **do** need to explain the complexity of your solutions. 

**Note:** the `main()` method in labs and assignments usually contains some 
code to run your program. Feel free to add, change, or comment anything in `main()` to help your development. 

### Implement the `Earthquake` class

Implement the `Earthquake` class, which will be used to store each earthquake record as a separate object. Add attributes to this class for each field in the CSV file.

- Add a `__repr__()` method to your Earthquake so that it shows a nicely-formatted string when you print it out. `__repr__()` is a special [built-in method](https://docs.python.org/3/library/functions.html#repr) that Python automatically calls when printing an object.


### Implement `load_data()`

In `EarthquakeDatabase`, read the `earthquakes.csv` file and store each record as an `Earthquake` instance in the existing `earthquakes` list. You can read this file the same way you did in Lab 1: open the file, create a `csv.reader()` over it, skip the header row with `next()`, and then iterate over each line in the file.

**Hints:**
- You will need to convert numeric fields to floating-point values using `float()` or integers using `int()`.
- There are two time fields in the CSV file: `time.epoch` and `time.full`, which both represent the same time in different ways. You only need to use one of these fields. 
- `time.epoch` is the time in milliseconds from the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time), a very common way to represent dates and times in computing. This is what the Python `time()` function returns. 
- `time.full` is a string-formatted date like humans would write. You can parse `time.full` in Python with `datetime.strptime(time_full_field, '%Y-%m-%d %H:%M:%S')`


### Implement `find_by_id()`

Find and return the first earthquake with the specified `id`. In this dataset, all earthquake IDs are guaranteed to be unique except for one.

- If no earthquake was found, return `None`.


### Implement `find_by_location()`

Find all earthquakes with the given `location` and return results in order from newest to oldest (this is the reverse of how they are ordered in the file).

- Do not modify the underlying list.
- `location` should be a case-insensitive match against the `location.name` field in the CSV (e.g., a search for "california" should match "California" but not "CA").
- If no earthquakes were found, return an empty list.

### Implement `find_strongest()`

Find and return the earthquake with the largest magnitude.


### Implement `find_nearby()`

Find all earthquakes in the specified area. Given an origin as `latitude` and `longitude` coordinates, and a `radius` within which to search, find all earthquakes whose `latitude` and `longitude` fall within this circle. 

This problem is slightly complicated because the Earth is not flat, it is (nearly) a sphere so we need to calculate distances over a 3-dimensional surface instead of a 2-dimensional plane. The distance between two points on a sphere is known as the [Great circle distance](https://en.wikipedia.org/wiki/Great-circle_distance), and we can calculate it using the well-known [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula):

$$\Delta \phi = (\phi_2 - \phi_1) / 2$$

$$\Delta \lambda = (\lambda_2 - \lambda_1) / 2$$

$$a = \sin^2(\Delta \phi) + \cos(\phi_1) * \cos(\phi_2) * \sin^2(\Delta 
\lambda)$$

$$c = 2 * atan2( \sqrt{a}, \sqrt{1 − a} )$$

$$d = R * c$$

Where $\phi$ is the latitude in radians, $\lambda$ is the longitude in radians, and $R$ is the radius of the earth in kilometers.

**Hints:**
- You can use any valid value for the Earth radius, for example the rectifying radius for the Earth radius is `6,367.445` km. Any result that is close enough will be okay.
- Convert latitude and longitude to radians using Python's `math.radians()` function.
- Review the [Python math module](https://docs.python.org/3/library/math.html) as it contains all the mathematical functions you will need.


### Implement `find_k_strongest()`

Find and return the `k` strongest earthquakes by magnitude.

- If `k` = 1, then this should return the same result as `find_strongest()`. 
- If `k` = 0, return an empty list.
- An inefficient solution is okay! Do not try to solve this with advanced Python structures like `heapq`. Do not modify the underlying `self.earthquakes` list.

**Hint:**
- You don't need to copy the array to solve this problem, but if you choose to you can use Python's native `copy()` method.


### Implement `find_duplicate()`

All the earthquakes in our dataset have a unique `id`. However, there are two earthquakes which share the same `id`. Find the duplicate `id` and return it.

### Implement `find_busiest_day()`

Find the 24 hour span in which the largest number of earthquakes occurred. Return the number of earthquakes within this 24-hour period.

- The underlying data is already sorted in chronological order.
- Using a sliding window, find the 24-hour span during which the most 
  earthquakes occurred. 
- The time window can (and does) span multiple days, it doesn't reset at midnight.

**Hint:** Python's [`datetime` module](https://docs.python.org/3/library/datetime.html) provides some useful utilities like `timedelta()` for comparing two dates. If your `Earthquake` times come from `time.epoch`, you can subtract the two values to get the delta between them, but remember they are in milliseconds (24 hours = 86,400,000 ms).


### Example output

```
Strongest earthquake: 2016-07-29 17:18:26 [us100068jg] Northern Mariana Islands, M7.7
Earthquakes in Oregon: 81
Earthquakes within 100 km of Corvallis: 4
Duplicate earthquake is: **********
Top 5 strongest earthquakes:
1. 2016-07-29 17:18:26 [us100068jg] Northern Mariana Islands, M7.7
2. 2016-08-19 03:32:22 [us10006exl] South Georgia Island region, M7.4
3. 2016-08-11 21:26:35 [us10006d5h] New Caledonia, M7.2
4. 2016-08-24 06:34:55 [us10006gbf] Burma, M6.8
5. 2016-08-20 23:45:23 [us10006fik] South Georgia Island region, M6.4
Busiest 24-hour window contains: *** earthquakes
```

**Note:** some values are censored so you can discover them for yourself.


## Part 2: Complexity analysis

For each of the following methods, provide a Big-O analysis of *both* its time complexity and storage complexity, where $N$ is the number of earthquakes. Use additional variables if needed and define what they represent.

- `load_data()`
- `find_by_location()`
- `find_by_id()`
- `find_strongest()`
- `find_nearby()`
- `find_k_strongest()` (this Big-O analysis should be defined in terms of $N$ and $k$)
- `find_duplicate()`
- `find_busiest_day()`


Write your answers in a file named `answers.txt`. Add it to your repository and commit it with the rest of your code.

## Submission instructions

- Ensure you have added your answers to `answers.txt`.
- Run `git add .` to add all changed files to the next commit.
- Run `git commit` to commit your work to the local repository.
- Run `git push` to upload your repository to Github. Please verify that all your work has actually been pushed and is accessible on github or you may not get credit for your work!
- Submit a link to your repository in canvas. Your work will be reviewed and manually graded.


## Acknowledgements

Earthquake data is from [CORGIS: The Collection of Really Great, Interesting, Situated Datasets](https://corgis-edu.github.io/corgis/csv/)
