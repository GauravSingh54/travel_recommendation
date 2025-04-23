window.addEventListener('DOMContentLoaded', function () {
    document.getElementById('state').addEventListener('change', function () {
        const selectedState = this.value;
        fetch('/get_cities', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ state: selectedState })
        })
            .then(response => response.json())
            .then(cities => {
                const citySelect = document.getElementById('city');
                citySelect.innerHTML = '<option value="">Select City</option>';
                cities.forEach(city => {
                    const option = document.createElement('option');
                    option.value = city;
                    option.text = city;
                    citySelect.appendChild(option);
                });
                document.getElementById('significance').innerHTML = '<option value="">Select Significance</option>';
                document.getElementById('best_time').innerHTML = '<option value="">Select Best Time</option>';
            });
    });

    document.getElementById('city').addEventListener('change', function () {
        const selectedCity = this.value;

        fetch('/get_significance', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ city: selectedCity })
        })
            .then(response => response.json())
            .then(data => {
                const sigSelect = document.getElementById('significance');
                sigSelect.innerHTML = '<option value="">Select Significance</option>';
                data.forEach(item => {
                    const option = document.createElement('option');
                    option.value = item;
                    option.text = item;
                    sigSelect.appendChild(option);
                });
            });

        fetch('/get_best_times', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ city: selectedCity })
        })
            .then(response => response.json())
            .then(data => {
                const btSelect = document.getElementById('best_time');
                btSelect.innerHTML = '<option value="">Select Best Time</option>';
                data.forEach(item => {
                    const option = document.createElement('option');
                    option.value = item;
                    option.text = item;
                    btSelect.appendChild(option);
                });
            });
    });
});