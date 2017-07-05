# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
===================
SBPy Thermal Module
===================

created on June 27, 2017
"""

__all__ = ['ThermalClass', 'STM', 'FRM', 'NEATM']


class ThermalClass():

    def flux(phys, eph, lam):
        """Model flux density for a given wavelength `lam`, or a list/array thereof

        Parameters
        ----------
        phys : `sbpy.data.Phys` instance, mandatory
            provide physical properties
        eph : `sbpy.data.Ephem` instance, mandatory
            provide object ephemerides
        lam : `astropy.units` quantity or list-like, mandatory
            wavelength or list thereof

        Examples
        --------
        >>> from astropy import Time
        >>> from astropy import units as u
        >>> from sbpy.thermal import STM
        >>> from sbpy.Data import Ephem, Phys
        >>> epoch = Time('2019-03-12 12:30:00', scale='utc')
        >>> eph = Ephem.from_horizons('2015 HW', '568', epoch)
        >>> phys = PhysProp('diam'=0.3*u.km, 'pv'=0.3)
        >>> lam = np.arange(1, 20, 5)*u.micron
        >>> flux = STM.flux(phys, eph, lam)

        not yet implemented

        """
        
    def fit(self, eph):
        """Fit thermal model to observations stored in `sbpy.data.Ephem` instance

        Parameters
        ----------
        eph : `sbpy.data.Ephem` instance, mandatory
            provide object ephemerides and flux measurements

        Examples
        --------
        >>> from sbpy.thermal import STM
        >>> stmfit = STM.fit(eph)
 
        not yet implemented

        """

        
class STM(ThermalClass):
    pass

class FRM(ThermalClass):
    pass

class NEATM(ThermalClass):
    pass