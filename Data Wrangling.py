
# Now on to Data Wrangling - chapter 7 of McKinney

# Example from book: movie lens data
# Three data sets, first the list of movies
PD.READ_TABLE
movies = pd.read_table(path + 'ml-1m/movies.dat',sep='::',names=['movie_id','title','genres'],engine='python')
# Second the list of ratings (this is big so use the nrows argument if it's slowing you down)
ratings = pd.read_table(path + 'ml-1m/ratings.dat',sep='::',names=['user_id','movie_id','rating','timestamp'])
# List of users
users = pd.read_table(path + 'ml-1m/users.dat',sep='::',names=['user_id','gender','age','occupation','zip'])

PD.MERGE
# First pd.merge - suppose we want to link together the details about the users and the ratings
# Note that the ratings DataFrame has lots of rows with the same users, see e.g.
ratings.head()

# So we now want each row to contain their rating and all their details
ratings_and_users = pd.merge(ratings,users) # notice how quick this is!
ratings_and_users.head(10)

# on, left_on, right_on arguments for merge
# Can specify the key on which to merge, but merge will automatically work this out if required
ratings_and_users = pd.merge(ratings,users,on='user_id')

# Notice that if I'd put in the column index differently I can specify the indices to match on for each data set
users_2 = pd.read_table(path+'ml-1m/users.dat',sep='::',engine='python',names=['userid','gender','rating','occupation','zip'])
ratings_and_users = pd.merge(ratings,users_2,left_on='user_id',right_on='userid')

# What if I had merged these the other way round?
other_merge = pd.merge(users,ratings,on='user_id')
# Works without error - does the same thing but puts the columns in a slightly different order

# multiple keys
# If you ahave multiple keys to match on, specify them as a list in the on argument

# Using the index as the merge key with left_index and right_index
# Sometimes you want to merge based on the indices, e.g. 
ratings_2 = pd.read_table(path + 'ml-1m/ratings.dat',sep='::',engine='python',names=['user_id','movie_id','rating','timestamp'],index_col='user_id')
users_2 = pd.read_table(path + 'ml-1m/users.dat',sep='::',engine='python',names=['user_id','gender','age','occupation','zip'],index_col='user_id')
# Can specify this explicitly in the merge
ratings_and_users_2 = pd.merge(ratings_2,users_2,left_index=True,right_index=True)

PD.CONCAT
## Concatenating data frames

# Back to the iphone/galaxy DataFrames
iphone_dict = {'Name': ['iPhone', 'iPhone 3G', 'iPhone 3GS', 'iPhone 4', 'iPhone 4S', 'iPhone 5', 'iPhone 5C', 'iPhone 5S'],
    'Memory_MB': [128, 128, 256, 512, 512, 1024, 1024, 1024],
    'Weight_g': [135, 133, 135, 137, 140, 112, 132, 112],
    'Camera_MP': [2, 2, 3, 5, 8, 8, 8, 8],
    'Year': [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2013] }
iphone_df = DataFrame(iphone_dict)

iphone_df = DataFrame(iphone_dict,index=iphone_dict['Year'])
galaxy_dict = {'Name': ['Galaxy S', 'Galaxy S II', 'Galaxy S III', 'Galaxy S 4', 'Galaxy S 5'],
    'Memory_MB': [512, 1024, 1024, 2048, 2048],
    'Weight_g': [119, 116, 133, 130, 145],
    'Camera_MP': [5, 8, 8, 13, 16],
    'Year': [2010, 2011, 2012, 2013, 2014] }
galaxy_df = DataFrame(galaxy_dict,index=galaxy_dict['Year'])

# Suppose we want to join these two together? How might we want to join them?
PD.CONCAT METTE I DATA FRAME UNO SOPRA L ALTRO

#note ignore_index=True   mette nuovi indici
# First consider stacking them on top of each other using concatenate
pd.concat([iphone_df,galaxy_df])
# What happens when the columns don't match exactly?
pd.concat([iphone_df.drop('Camera_MP',axis=1),galaxy_df])
# Can give it more than two objects
pd.concat([iphone_df,galaxy_df,iphone_df])

JOIN  METTE UNO ACCANTO ALL'ALTRO 
# What if instead we wanted it joined by year? Could use join
iphone_df.join(galaxy_df,lsuffix='x')
# Or you could go back to merge
pd.merge(iphone_df,galaxy_df,on='Year',how='outer')
# Note the how='outer' means it doesn't throw away any rows where things don't match

#NEAT
# Another useful function for combining DataFrames is combine_first:
iphone_df.combine_first(galaxy_df)
galaxy_df.combine_first(iphone_df)
# Can you see what it is doing? It's merging the indices and then fillin in the 
# missing values from the other DataFrame - neat!

################################################################################
DUPLICATE

# Removing duplicates with .duplicated() and drop_duplicates()

# Let's play around again with the users movie lens function

# First re-load the data in case you've lost it
ratings = pd.read_table(path + 'ml-1m/ratings.dat',sep='::',engine='python',names=['user_id','movie_id','rating','timestamp'])

# Let's find out how many user IDs are duplicated, i.e. have multiple reviews
ratings.user_id.duplicated()
# A bit long
ratings.user_id.duplicated().sum() #994169
ratings.user_id.duplicated().value_counts() # 994169!

# Drop the duplicates
ratings.user_id.drop_duplicates() # Lenght 6040 that is values not duplicated
# An alternative to this that is perhaps neater is:
ratings.drop_duplicates('user_id')

MAPPING
# Mapping data 
# Let's have a look at the users data again, specifically the age column
users = pd.read_table(path + 'ml-1m/users.dat',sep='::',engine='python',names=['user_id','gender','age','occupation','zip'])
users.age.value_counts()
# The README file in the movie lens folder says that these correspond to:
#  1:  "Under 18"
# 18:  "18-24"
# 25:  "25-34"
# 35:  "35-44"
# 45:  "45-49"
# 50:  "50-55"
# 56:  "56+"

# Let's create a mapping dict:
my_map = {1:'Under 18',18:'18-24',25:'25-34',35:'35-44',45:'45-49',50:'50-55',56:'56+'}
users['age_grp'] = users['age'].map(my_map)
users.head()

# You can also use a lambda function
users['age_grp_2'] = users['age'].map(lambda x: my_map[x])

# Yet another alternative for doing this in place is replace
users['age'] = users['age'].replace([1,18,25,35,45,50,56],['Under 18','18-24','25-34','35-44','45-49','50-55','56+'])

PD.CUT
# The cut method
# Let's suppose we had raw ages rather than age groups above and wanted to group
# them in the same way
ages = Series(npr.poisson(lam=40,size=100))
bins = [0,20,40,60]
age_groups = pd.cut(ages,bins)

# For some reason this is a special type of Categorical object
type(age_groups)
pd.value_counts(age_groups)

# You can even give these labels:
age_groups = pd.cut(ages,bins,labels=['Young','Middle-aged','Old'])
pd.value_counts(age_groups)

# Or you can give cut just a number of bins 
pd.cut(ages,4,precision=0)
# Or use qcut which cuts by quantiles
pd.qcut(ages,4) # quartiles
# You can give qcut your own quantiles
pd.qcut(ages,[0.,0.25,0.5,0.75,1.]) 

# To finish off - a useful little trick the get_dummies method for
# creating indicator variables (i.e. 0s and 1s) categorical variables
# This is widely used in regression and classification

PD.GET_DUMMIES
# Suppose we wanted to turn the rating column in the ratings DataFrame
# into indicator variables:
pd.get_dummies(ratings['rating'])
# Combining get dummies with cut can also be usefulk
