# NumPy Array Copy vs View
<!DOCTYPE html>
<html>
<body>
    <ol>
        <li>
            <h2>The Difference Between Copy and View</h2>
            <p>The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.</p>
            <p>The copy owns the data and any changes made to the copy will not affect the original array, and any changes made to the original array will not affect the copy.</p>
            <p>The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.</p>
        </li>
    </ol>
</body>
</html>