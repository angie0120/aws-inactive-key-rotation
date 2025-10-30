def analyze_all_access_keys(self):
    print("🔍 Starting comprehensive access key analysis...")
    users = self.get_all_iam_users()
    if not users:
        print("⚠️  No IAM users found or unable to retrieve users")
        return None
    
    # Analysis logic continues... (truncated for brevity)
    
    print(f"📊 Analysis complete:")
    print(f"  - Total users: {analysis_results['summary']['total_users']}")
    print(f"  - Users with keys: {analysis_results['summary']['users_with_keys']}")
    print(f"  - Total keys: {total_keys}")
    print(f"  - Critical risk: {analysis_results['summary']['critical_keys']}")
    print(f"  - High risk: {analysis_results['summary']['high_risk_keys']}")
    print(f"  - Compliance rate: {compliance_rate}%")
    return analysis_results