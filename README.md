# multi-region-api-gateway-dynamodb
multi-region-api-gateway-dynamodb

![image](https://user-images.githubusercontent.com/39345855/168690142-1384d5f7-2950-4556-becf-09577222e9dd.png)

# Step 1 : Install Serverless Framework 

```
npm install -g serverless
serverless config credentials --provider aws --key XXXX  --secret XXXXX -o

```
# Step 2: Create DynamoDB Tables 

```
cd dynamodb-deployment
sls deploy
```

# Step 3: Populate DynamoDB with fake Data

```
cd dynamodb-populate

pip install pynamodb

python run.py
```

# Step 4:  Deploy
```
cd microservice
> sls plugin install -n serverless-python-requirements
> npm i -D serverless-dotenv-plugin

##### make sure to change ENV VAR too 
sls deploy --region='us-east-1'

##### make sure to change ENV VAR too 
sls deploy --region='us-west-2'

```
