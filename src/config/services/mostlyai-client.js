import axios from 'axios';
import { mostlyAiConfig, validateConfig } from '../config/mostly-ai.js';

class MostlyAiClient {
  constructor() {
    validateConfig();
    
    this.client = axios.create({
      baseURL: mostlyAiConfig.baseUrl,
      timeout: mostlyAiConfig.timeout,
      headers: {
        'Authorization': `Bearer ${mostlyAiConfig.apiKey}`,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    });

    // Add request interceptor for logging
    this.client.interceptors.request.use(
      (config) => {
        console.log(`Making request to: ${config.method?.toUpperCase()} ${config.url}`);
        return config;
      },
      (error) => {
        console.error('Request error:', error);
        return Promise.reject(error);
      }
    );

    // Add response interceptor for error handling
    this.client.interceptors.response.use(
      (response) => {
        console.log(`Response received: ${response.status} ${response.statusText}`);
        return response;
      },
      (error) => {
        console.error('Response error:', error.response?.data || error.message);
        return Promise.reject(error);
      }
    );
  }

  async testConnection() {
    try {
      const response = await this.client.get('/health');
      return {
        success: true,
        status: response.status,
        message: 'Connection successful'
      };
    } catch (error) {
      return {
        success: false,
        status: error.response?.status || 500,
        message: error.response?.data?.message || error.message
      };
    }
  }

  async getWorkspaces() {
    try {
      const response = await this.client.get('/workspaces');
      return response.data;
    } catch (error) {
      throw new Error(`Failed to get workspaces: ${error.message}`);
    }
  }

  async getDatasets(workspaceId = mostlyAiConfig.workspaceId) {
    try {
      const response = await this.client.get(`/workspaces/${workspaceId}/datasets`);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to get datasets: ${error.message}`);
    }
  }

  async createSyntheticDataJob(config) {
    try {
      const response = await this.client.post('/synthetic-data/jobs', config);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to create synthetic data job: ${error.message}`);
    }
  }

  async getJobStatus(jobId) {
    try {
      const response = await this.client.get(`/synthetic-data/jobs/${jobId}`);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to get job status: ${error.message}`);
    }
  }

  async downloadSyntheticData(jobId, outputPath) {
    try {
      const response = await this.client.get(`/synthetic-data/jobs/${jobId}/download`, {
        responseType: 'stream'
      });
      
      return new Promise((resolve, reject) => {
        const writer = fs.createWriteStream(outputPath);
        response.data.pipe(writer);
        
        writer.on('finish', () => resolve(outputPath));
        writer.on('error', reject);
      });
    } catch (error) {
      throw new Error(`Failed to download synthetic data: ${error.message}`);
    }
  }
}

export default MostlyAiClient;