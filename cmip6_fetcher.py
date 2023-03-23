import os
import urllib.request


variable_id = 'tas'
date = '202304'
experiment_id = 'ssp245'
time_range = 'monthly'
model_id = 'GISS-E2-1-G'
member_id = 'r1i1p1f2'
if time_range == 'monthly':
    url = f'https://nex-gddp-cmip6-cog.s3-us-west-2.amazonaws.com/monthly/CMIP6_ensemble_median/{variable_id}/{variable_id}_month_ensemble-median_{experiment_id}_{date}.tif'
elif time_range == 'day':
    url = f'https://nex-gddp-cmip6-cog.s3-us-west-2.amazonaws.com/daily/{model_id}/{experiment_id}/r1i1p1f2/tas/tas_day_GISS-E2-1-G_ssp245_r1i1p1f2_gn_2015_01_01.tif'


try:
    with urllib.request.urlopen(url) as f:
        geotiff_raw = f.read()
        with open(os.path.basename(url), 'wb') as file:
            file.write(geotiff_raw)
except Exception as e:
    print(f'{url} was not found')


# NASA has published a daily and monthly aggregated subset of CMIP6 (nex-gddp-cmip6) which I can get easy access to on AWS. For CMIP5 I've been using the google earth engine to do almost all the calculations, but with AWS I'd need to do them locally -- that is probably fine seeing as how fast they were when we needed to do something local a while back.
#
# The downside of the CMIP6 is that it doesn't have the exact time domain breakdowns like you'd asked in that previous thread. I'm thinking maybe you just wanted to see them as much as you didn't necessarily NEED 3 hour time domain resolution on a modeled global precip dataset? If so that's great because here's what we have on daily and monthly timesteps:
#
# ; hurs - Near-Surface Relative Humidity percentage
# ; huss - Near-Surface Specific Humidity dimensionless ratio (kg/kg)
# ; pr- Precipitation (mean of the daily precipitation rate) kg m-2 s-1
# ; rlds - Surface Downwelling Longwave Radiation W m-2
# ; rsds - Surface Downwelling Shortwave Radiation W m-2
# ; sfcWind - Daily-Mean Near-Surface Wind Speed m s-1
# ; tas - Daily Near-Surface Air Temperature Degrees Kelvin
# ; tasmax - Daily Maximum Near-Surface Air Temperature Degrees Kelvin
# ; tasmin - Daily Minimum Near-Surface Air Temperature Degrees Kelvin
#