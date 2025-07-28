import MostlyAiClient from './services/mostly-ai-client.js';
import { mostlyAiConfig } from './config/mostly-ai.js';

async function main() {
  console.log('🎯 Mostly AI CI/CD Integration\n');

  try {
    console.log('Initializing Mostly AI client...');
    const client = new MostlyAiClient();

    // Test connection
    const connectionTest = await client.testConnection();
    if (!connectionTest.success) {
      throw new Error(`API connection failed: ${connectionTest.message}`);
    }

    console.log('✅ Successfully connected to Mostly AI API');
    console.log('\nAvailable commands:');
    console.log('- npm run test: Test API connection');
    console.log('- npm run generate-data: Generate synthetic data');
    console.log('- npm run validate-data: Validate generated data');

    console.log('\nConfiguration:');
    console.log(`- Base URL: ${mostlyAiConfig.baseUrl}`);
    console.log(`- Workspace ID: ${mostlyAiConfig.workspaceId || 'Not configured'}`);

  } catch (error) {
    console.error('❌ Initialization failed:', error.message);
    console.log('\nPlease check your configuration in .env file');
    process.exit(1);
  }
}

main();