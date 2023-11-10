# NumPy ufuncs
<!DOCTYPE html>
<html>
<body>
    <ol>
        <li>
            <h2>What are ufuncs?</h2>
            <p>ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the <code>ndarray</code> object.</p>
            <h2>Why use ufuncs?</h2>
            <pre>
ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.

They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

<code>ufuncs</code> also take additional arguments, like:

<code>where</code> boolean array or condition defining where the operations should take place.

<code>dtype</code> defining the return type of elements.

<code>out</code> output array where the return value should be copied.
            </pre>
            <h2>What is Vectorization?</h2>
            <pre>
Converting iterative statements into a vector-based operation is called vectorization.

It is faster as modern CPUs are optimized for such operations.

Add the Elements of Two Lists
list 1: [1, 2, 3, 4]

list 2: [4, 5, 6, 7]

One way of doing it is to iterate over both of the lists and then sum each elements.


            </pre>
        </li>
    </ol>
</body>
</html>