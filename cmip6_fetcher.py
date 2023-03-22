import os
import urllib.request


variable_id = 'tas'
date = '202304'
experiment_id = 'ssp245'
url = f'https://nex-gddp-cmip6-cog.s3-us-west-2.amazonaws.com/monthly/CMIP6_ensemble_median/{variable_id}/{variable_id}_month_ensemble-median_{experiment_id}_{date}.tif'

try:
    with urllib.request.urlopen(url) as f:
        geotiff_raw = f.read()
        with open(os.path.basename(url), 'wb') as file:
            file.write(geotiff_raw)
except Exception as e:
    print(f'{url} was not found')
