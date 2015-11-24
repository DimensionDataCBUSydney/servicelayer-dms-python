class DmsRequestError(Exception):
    def __init__(self, error_message, status_code):
        self.message = "Error requesting DMS API %s with code %s" \
              % (error_message, status_code)
        super(DmsRequestError, self).__init__(self.message)
