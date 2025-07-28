import dotenv from 'dotenv';

// Load environment variables
dotenv.config();

export const mostlyAiConfig = {
  apiKey: process.env.MOSTLY_AI_API_KEY,
  baseUrl: process.env.MOSTLY_AI_BASE_URL || 'https://app.mostly.ai/api/v1',
  workspaceId: process.env.MOSTLY_AI_WORKSPACE_ID,
  timeout: 30000,
  retryAttempts: 3,
  retryDelay: 1000
};