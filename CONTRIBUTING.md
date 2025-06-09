# Contributing to Stable Diffusion Streamlit

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the Stable Diffusion Streamlit application.

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.8+
- Git

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/LowinLi/stable-diffusion-streamlit.git
   cd stable-diffusion-streamlit
   ```

2. **Set up development environment**
   ```bash
   # Install dependencies
   pip install -r src/stable-diffusion-streamlit/requirements.txt
   
   # Run with Docker Compose
   docker-compose up -d
   ```

3. **Access the application**
   - Open http://localhost:8501 in your browser

## 📝 How to Contribute

### Reporting Issues

- Use the GitHub issue tracker to report bugs
- Include detailed information about your environment
- Provide steps to reproduce the issue
- Include screenshots if applicable

### Submitting Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the existing code style
   - Add tests if applicable
   - Update documentation as needed

3. **Test your changes**
   ```bash
   # Test the Docker build
   docker-compose build
   docker-compose up -d
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## 🎯 Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused

### Commit Messages

Use conventional commit format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

### Docker Best Practices

- Keep Docker images lightweight
- Use multi-stage builds when appropriate
- Document any new environment variables
- Test Docker builds locally

## 🔍 Testing

- Test the application with different prompts
- Verify Docker container functionality
- Check memory usage and performance
- Test on different platforms if possible

## 📚 Documentation

- Update README.md for new features
- Add inline code comments
- Update Docker documentation
- Include examples for new functionality

## 🤝 Community

- Be respectful and inclusive
- Help others in discussions
- Share knowledge and best practices
- Follow the project's code of conduct

## 📞 Getting Help

- Check existing issues and discussions
- Create a new issue for questions
- Join community discussions
- Contact maintainers if needed

Thank you for contributing to make this project better! 🎉