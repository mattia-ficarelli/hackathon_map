<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

## Multiverse Hackathon: Finding the best location to open a company’s first operational facility.

 The CTO of an on-demand delivery start-up based in Greater London is looking to open the company’s first operational facility. The company uses a fleet of electric scooters to provide a “last-mile” delivery service to Fortune 500 companies in the city. The executive sponsor has asked you to make a recommendation about where to open the first location, based on the following criteria:
 - Location with the lowest rent.
 - Within the London ultra-low emission zone.
 - 20 minutes from both the City and Canary Warf.

<hr class="nhsuk-u-margin-top-0 nhsuk-u-margin-bottom-6">

{% include update.html %}

## Our solution:

- The following map displays the London area.
- Average rent prices per month (£) for each London postcode are represented on a colour scale, the darker the colour, the higher the rent. 
- The large red area visible on the map represents London’s ultra-low emission zone (October 2021).
- The two red markers on the map represent the City of London, and Canary Wharf, the key locations used in our proximity analysis
- The purple markers on the map represent potential postcode areas that meet all of the requirements of the business case.
- The green marker on the map represents the postcode area with the cheapest average monthly rent while meeting all the requirements of the business case.

<iframe width= "900" height="700"  src="assets/folium/folium_obj.html" style="border:none;"></iframe>

<div class="nhsuk-warning-callout">
  <h3 class="nhsuk-warning-callout__label">
    Data Quality Notice<span class="nhsuk-u-visually-hidden">:</span>
  </h3>
  <p>Postcode areas highlighted in black on the London map had no available rent data.
  </p>
</div>

<hr class="nhsuk-u-margin-top-0 nhsuk-u-margin-bottom-6">

This page is built using end-to-end open source analytical tools including: [python](https://www.python.org/), [folium](http://python-visualization.github.io/folium/), [github.io](https://pages.github.com/), and [github actions](https://github.com/features/actions).

If you have any suggestions or questions, email: <a href="mailto:mattia.ficarelli@gmail.com">mattia.ficarelli@gmail.com</a>

<hr class="nhsuk-u-margin-top-0 nhsuk-u-margin-bottom-6">
