class Plugin:
    def __init__(self):
        """Initialise the plugin.
        Use the constructor to set up any required attributes needed for the plugin.
        The constructor is run whenever CURATE or ANNOTATE are loaded for a project with this plugin enabled.
        """
        pass

    def __call__(self, image, metadata, annotations):
        """Run the plugin.
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


        return image, metadata, annotations
