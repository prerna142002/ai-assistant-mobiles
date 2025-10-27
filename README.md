# Mobile Shopping Chat Agent

An AI-powered conversational agent that helps users find and compare mobile phones based on their preferences.

## Features
- Natural language understanding for mobile phone queries
- Intent classification to understand user requests
- Mobile phone database with filtering capabilities
- Conversational interface for easy interaction
- RESTful API for integration with frontend applications

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file based on `.env.example` and fill in your configuration
4. Run the application:
   ```bash
   python app.py
   ```

## Deployment

### Prerequisites
- Python 3.8+
- Git
- Supabase
- Gemini API Key

### Deploying to Render.com

1. **Prepare your code**
   - Make sure all your changes are committed to a Git repository
   - Push your code to GitHub, GitLab, or Bitbucket

3. **Deploy to Render**
   - Sign up at [Render](https://render.com/) if you haven't already
   - Click "New" and select "Web Service"
   - Connect your repository
   - Configure the deployment:
     - Name: `mobile-shopping-agent`
     - Region: Choose the one closest to your users
     - Branch: `main` or your preferred branch
     - Build Command: `pip install -r requirements.txt`
   - Add environment variables from your `.env` file
   - Click "Create Web Service"

4. **Set up custom domain (optional)**
   - Go to your service settings
   - Click "Add Custom Domain" and follow the instructions

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

## Project Structure

```
.
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── .env.example         # Example environment variables
├── models/              # ML models for intent classification
├── utils/               # Utility functions
├──────── agent.py              # Chat agent implementation
├──────── data_loader.py        # Data loading and querying
└── data/                # Sample mobile phone dataset
```

## API Documentation

### Start a conversation
```
POST /api/chat
{
    "message": "I'm looking for an iPhone under $1000"
}
```

### Response Format
```json
{
    "response": "Here are some iPhones under $1000...",
    "suggestions": ["Show more", "Filter by storage", "Compare models"],
    "products": [...]
}
```

## Troubleshooting

- **Application not starting**: Check the logs in your hosting provider's dashboard
- **Database connection issues**: Verify your `MONGODB_URI` is correct and the database is accessible
- **Dependency issues**: Make sure all dependencies are installed with the correct versions
