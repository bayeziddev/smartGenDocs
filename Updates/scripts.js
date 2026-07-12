/**
 * SmartGen Changelog Loader
 * Handles dynamic data fetching from /data/changelog.json
 */

document.addEventListener('DOMContentLoaded', () => {
    loadChangelog();
});

async function loadChangelog() {
    const timeline = document.getElementById('timeline');
    
    // পাথটি নিশ্চিত করুন আপনার প্রজেক্টের রুট থেকে
    const jsonPath = '/data/changelog.json'; 

    try {
        const response = await fetch(jsonPath);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const changelog = await response.json();
        
        if (!changelog || !Array.isArray(changelog) || changelog.length === 0) {
            renderEmptyState(timeline);
            return;
        }

        // Sort: Newest date first
        changelog.sort((a, b) => new Date(b.date) - new Date(a.date));

        // Render timeline
        timeline.innerHTML = changelog.map(entry => `
            <div class="timeline-item">
                <div class="timeline-marker"></div>
                <div class="timeline-content">
                    <div class="timeline-date">${formatDate(entry.date)}</div>
                    <h3 class="timeline-title">${escapeHtml(entry.version || '')} ${escapeHtml(entry.title)}</h3>
                    <ul class="timeline-description">
                        ${renderChanges(entry)}
                    </ul>
                </div>
            </div>
        `).join('');

    } catch (error) {
        console.error('Error loading changelog:', error);
        timeline.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">⚠️</div>
                <p>Failed to load updates. Please check if <strong>${jsonPath}</strong> exists and is valid JSON.</p>
            </div>
        `;
    }
}

// Helper: Handle array of changes or single description
function renderChanges(entry) {
    if (entry.changes && Array.isArray(entry.changes)) {
        return entry.changes.map(c => `<li>${escapeHtml(c)}</li>`).join('');
    }
    return `<li>${escapeHtml(entry.description || 'No details provided.')}</li>`;
}

function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString('en-US', { 
        year: 'numeric', month: 'long', day: 'numeric' 
    });
}

function escapeHtml(text) {
    const p = document.createElement('p');
    p.textContent = text;
    return p.innerHTML;
}

function renderEmptyState(container) {
    container.innerHTML = `
        <div class="empty-state">
            <div class="empty-state-icon">📭</div>
            <p>No updates yet. Check back soon for exciting new features!</p>
        </div>
    `;
}