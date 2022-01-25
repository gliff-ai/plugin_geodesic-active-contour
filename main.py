import gliff_sdk as gliff
import numpy as np
from skimage import img_as_float
from skimage.segmentation import (morphological_geodesic_active_contour,
                                  inverse_gaussian_gradient,
                                  checkerboard_level_set)

class Plugin:
    def __init__(self):
        """Initialise the plugin.
        Use the constructor to set up any required attributes needed for the plugin.
        The constructor is run whenever CURATE or ANNOTATE are loaded for a project with this plugin enabled.
        """
        pass

    def __call__(self, image, metadata, annotations):
        """Run morphological geodesic active contours for segmentation.
        Basically nicked from: 
        Use the call method to run your code.
        Inputs:
            image: a PIL Image object
            metadata: a dictionary of metadata
            annotations: a list of annotation objects
        Outputs:
            tuple of updated - 
                image: a PIL Image object
                metadata: a dictionary of metadata
                annotations: a list of annotation objects
        """

        # Convert image to float
        image = img_as_float(image)

        # Calculate gradient image
        gradient_image = inverse_gaussian_gradient(image)

        # Initial level set
        initial_level_set = np.zeros(image.shape, dtype=np.int8)
        initial_level_set[10:-10, 10:-10] = 1

        # List with intermediate results for plotting the evolution
        level_set = morphological_geodesic_active_contour(gradient_image,
                                                          num_iter=230,
                                                init_level_set=initial_level_set,
                                                smoothing=1, balloon=-1,
                                                threshold=0.69)

        # add level set to annotations as spline
        gliff.add_annotation(annotations, level_set, toolbox="spline")

        return image, metadata, annotations
