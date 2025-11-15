import numpy as np
import climlab

# -- set up simple 1-D column with Manabe H2O + RRTMG
state = climlab.column_state(num_lev=30)
h2o = climlab.radiation.ManabeWaterVapor(state=state)
rad = climlab.radiation.RRTMG(state=state, specific_humidity=h2o.q, albedo=0.25)
model = climlab.couple([rad, h2o])

# -- integrate ~2 years to (near) equilibrium
model.integrate_years(2)

# -- small helper to safely get a float out of a Field / memoryview / np array
def to_float(x):
    raw = getattr(x, "data", x)          # Field -> raw data
    arr = np.array(raw)                  # memoryview/array/scalar -> np.array
    return float(arr.squeeze().reshape(-1)[0])

asr = to_float(model.ASR)
olr = to_float(model.OLR)
ts  = to_float(model.Ts)

print(f"ASR - OLR = {asr - olr:.2f} W/m² | Ts = {ts:.2f} K")



