# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies for sql execution
from .sql_execution import query

# Create a subclass of QueryBase
# called  `Team`
class Team(QueryBase):

    # Set the class attribute `name`
    # to the string "team"
    name = "team"

    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    @query
    def names(self):
        """
        Return all team names and ids.
        """
        
        # Query 5
        return """
        SELECT team_name, team_id
        FROM team
        """

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    @query
    def username(self, id):
        """
        Return the name of a specific team.
        """

        # Query 6
        return f"""
        SELECT team_name
        FROM team
        WHERE team_id = {id}
        """

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    def model_data(self, id):
        """
        Return model input data for all employees in a team as a pandas DataFrame.
        """

        sql_query = f"""
            SELECT positive_events, negative_events FROM (
                    SELECT employee_id
                         , SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                    GROUP BY employee_id
                   )
                """

        return self.pandas_query(sql_query)