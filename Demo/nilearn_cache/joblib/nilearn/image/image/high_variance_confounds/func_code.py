# first line: 28
def high_variance_confounds(imgs, n_confounds=5, percentile=2.,
                            detrend=True, mask_img=None):
    """ Return confounds signals extracted from input signals with highest
        variance.

        Parameters
        ----------
        imgs: Niimg-like object
            See http://nilearn.github.io/manipulating_images/input_output.html
            4D image.

        mask_img: Niimg-like object
            See http://nilearn.github.io/manipulating_images/input_output.html
            If provided, confounds are extracted from voxels inside the mask.
            If not provided, all voxels are used.

        n_confounds: int
            Number of confounds to return

        percentile: float
            Highest-variance signals percentile to keep before computing the
            singular value decomposition, 0. <= `percentile` <= 100.
            mask_img.sum() * percentile / 100. must be greater than n_confounds.

        detrend: bool
            If True, detrend signals before processing.

        Returns
        -------
        v: numpy.ndarray
            highest variance confounds. Shape: (number of scans, n_confounds)

        Notes
        ------
        This method is related to what has been published in the literature
        as 'CompCor' (Behzadi NeuroImage 2007).

        The implemented algorithm does the following:

        - compute sum of squares for each signals (no mean removal)
        - keep a given percentile of signals with highest variance (percentile)
        - compute an svd of the extracted signals
        - return a given number (n_confounds) of signals from the svd with
          highest singular values.

        See also
        --------
        nilearn.signal.high_variance_confounds
    """
    from .. import masking

    if mask_img is not None:
        sigs = masking.apply_mask(imgs, mask_img)
    else:
        # Load the data only if it doesn't need to be masked
        imgs = check_niimg_4d(imgs)
        sigs = as_ndarray(imgs.get_data())
        # Not using apply_mask here saves memory in most cases.
        del imgs  # help reduce memory consumption
        sigs = np.reshape(sigs, (-1, sigs.shape[-1])).T

    return signal.high_variance_confounds(sigs, n_confounds=n_confounds,
                                          percentile=percentile,
                                          detrend=detrend)
