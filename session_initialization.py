def initialize_aws_session(self):
    try:
        if self.profile_name:
            print(f"🔐 Initializing AWS session with profile: {self.profile_name}")
            self.session = boto3.Session(profile_name=self.profile_name, region_name=self.region)
        else:
            print("🔐 Initializing AWS session with default credentials")
            self.session = boto3.Session(region_name=self.region)
        self.iam_client = self.session.client('iam')
        sts_client = self.session.client('sts')
        caller_identity = sts_client.get_caller_identity()
        self.account_id = caller_identity['Account']
        print(f"✅ Successfully connected to AWS Account: {self.account_id}")
        return True
    except ProfileNotFound:
        print(f"❌ Error: AWS profile '{self.profile_name}' not found")
        return False
    except NoCredentialsError:
        print("❌ Error: No AWS credentials found")
        return False