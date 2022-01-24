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
            image: A PIL Image object.
            metadata: A dictionary of metadata.
        Outputs:
            tuple of - 
                image: A PIL Image object.
                metadata: A dictionary of metadata.
        """


        return image, metadata, annotations
