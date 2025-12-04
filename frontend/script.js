const API_URL = 'http://localhost:8000';

async function analyzeText() {
    const textInput = document.getElementById('textInput');
    const text = textInput.value.trim();
    
    if (!text) {
        alert('Por favor escribe un texto para analizar');
        return;
    }
    
    const analyzeBtn = document.getElementById('analyzeBtn');
    const loading = document.getElementById('loading');
    const resultSection = document.getElementById('resultSection');
    
    analyzeBtn.disabled = true;
    loading.classList.remove('hidden');
    resultSection.classList.add('hidden');
    
    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });
        
        if (!response.ok) {
            throw new Error('Error en la peticion');
        }
        
        const result = await response.json();
        displayResult(result);
        loadHistory();
        
    } catch (error) {
        alert('Error al analizar el texto: ' + error.message);
    } finally {
        analyzeBtn.disabled = false;
        loading.classList.add('hidden');
    }
}

function displayResult(result) {
    const resultSection = document.getElementById('resultSection');
    const resultContent = document.getElementById('resultContent');
    
    const statusClass = result.is_toxic ? 'toxic' : 'non-toxic';
    const statusText = result.is_toxic ? '⚠️ TOXICO' : '✅ NO TOXICO';
    
    let labelsHtml = '';
    for (const [label, score] of Object.entries(result.labels)) {
        const percentage = (score * 100).toFixed(2);
        labelsHtml += `
            <div class="label-item">
                <span class="label-name">${label}</span>
                <span class="label-score">${percentage}%</span>
            </div>
        `;
    }
    
    resultContent.innerHTML = `
        <div class="result-box">
            <div class="result-text">"${result.text}"</div>
            <div class="result-status ${statusClass}">${statusText}</div>
            <p><strong>Categoria principal:</strong> ${result.main_category}</p>
            <p><strong>Confianza:</strong> ${(result.confidence * 100).toFixed(2)}%</p>
        </div>
        <div class="result-box">
            <h3>Desglose por Categoria</h3>
            <div class="labels-grid">
                ${labelsHtml}
            </div>
        </div>
    `;
    
    resultSection.classList.remove('hidden');
}

async function loadHistory() {
    const historyContent = document.getElementById('historyContent');
    
    try {
        const response = await fetch(`${API_URL}/history?limit=10`);
        
        if (!response.ok) {
            throw new Error('Error al cargar historial');
        }
        
        const data = await response.json();
        
        if (data.predictions.length === 0) {
            historyContent.innerHTML = '<p style="text-align: center; color: #777;">No hay predicciones aun</p>';
            return;
        }
        
        let historyHtml = '';
        for (const pred of data.predictions) {
            const itemClass = pred.is_toxic ? 'toxic-item' : '';
            const statusEmoji = pred.is_toxic ? '⚠️' : '✅';
            const date = new Date(pred.timestamp).toLocaleString('es-ES');
            
            historyHtml += `
                <div class="history-item ${itemClass}">
                    <div class="history-text">${statusEmoji} "${pred.text}"</div>
                    <div class="history-meta">
                        <span>${pred.main_category} (${(pred.confidence * 100).toFixed(1)}%)</span>
                        <span>${date}</span>
                    </div>
                </div>
            `;
        }
        
        historyContent.innerHTML = historyHtml;
        
    } catch (error) {
        historyContent.innerHTML = '<p style="color: red;">Error al cargar el historial</p>';
    }
}

document.getElementById('textInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        analyzeText();
    }
});

window.onload = function() {
    loadHistory();
};
