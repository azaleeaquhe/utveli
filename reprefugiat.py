def return_result(result):
  """Returns the result of a function.

  This function is used to return the result of a function that is called from
  another function. The result is returned as a dictionary, which contains the
  following keys:

  * `result`: The result of the function.
  * `error`: An error message, if any.

  Args:
    result: The result of the function.

  Returns:
    A dictionary containing the result and error message.
  """

  return {"result": result, "error": None}
