import pandas as pd

# compute the by quarter totals for each measure
totals = FDIC_SDI_panel.sum()

# compute the base quarter totals for each measure
base_qtr='2013-12'
totals_base_qtr = totals.copy()
totals_base_qtr[:] = totals[base_qtr]
totals_base_qtr.fillna(method='bfill', inplace=True)

def janicki_prescott_norm(item):
    """
    In order to make sure results are comparable across years, I follow 
    Janicki and Prescott (2006) and deflate and re-scale each measure of bank 
    size by dividing by banking sector totals relative to some base quarter. 
    Specifically, let :math:`S_{i,t}^{raw}` denote the raw size of bank :math:`i`
    in year :math:`t` based on one of the six size measures detailed above. The 
    normalized size of bank :math:`i` relative to the base quarter is defined as
    follows:
             
    .. math::
    
        S_{i,t}^{norm} = \frac{S_{i,t}^{raw}}{\sum_{j}S_{j,t}^{raw}}\sum_{j}S_{i,base}^{raw}
    
    where :math:\sum_{j}S_{j,t}^{raw}` is the banking sector total of some size 
    measure in year :math:`t` (i.e., total banking sector assets in year :math:`t`), 
    and :math:`\sum_{j}S_{j,base}^{raw}` is the banking sector total of the same
    size measure in the base quarter.
    
    """
    return (FDIC_SDI_panel[item] / totals[item]) * totals_base_qtr[item]

# apply the Janicki and Prescott (2006) normalized size measure 
for item in FDIC_SDI_panel.items:
    FDIC_SDI_panel[item] = janicki_prescott_norm(item)
    
# pickle the object for later use!
FDIC_SDI_panel.to_pickle('FDIC_SDI_normed_panel.pkl')
