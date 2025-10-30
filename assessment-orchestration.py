def run_assessment(self):
    print("🚀 Starting AWS Access Key Lifecycle Assessment")
    print("=" * 60)
    if not self.initialize_aws_session():
        return False
    analysis_results = self.analyze_all_access_keys()
    if not analysis_results:
        print("❌ Failed to analyze access keys")
        return False
    print("\n📋 Generating compliance reports...")
    json_report = self.generate_json_report(analysis_results)
    self.save_json_report(json_report)
    self.save_csv_report(analysis_results)
    # Output summary
    print("\n" + "=" * 60)
    print("📊 ASSESSMENT SUMMARY")
    print("=" * 60)
    print(f"Account ID: {self.account_id}")
    print(f"Total Users: {analysis_results['summary']['total_users']}")
    print(f"Total Access Keys: {analysis_results['summary']['total_keys']}")
    print(f"Critical Risk Keys: {analysis_results['summary']['critical_keys']}")
    print(f"High Risk Keys: {analysis_results['summary']['high_risk_keys']}")
    print(f"Never Used Keys: {analysis_results['summary']['never_used_keys']}")
    print(f"Compliance Rate: {analysis_results['summary']['compliance_rate']}%")
    overall_status = json_report['compliance_assessment']['overall_status']
    print(f"Overall Status: {overall_status}")
    if overall_status == 'COMPLIANT':
        print("✅ Access key management meets compliance requirements!")
    else:
        print("⚠️  Access key management requires attention - see recommendations above")
    return True